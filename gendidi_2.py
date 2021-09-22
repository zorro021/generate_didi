#-*- coding:utf-8 -*-
'''
 Version:   0.2
 Date:      2021-06-03
 Author:    Nobody
 Description:
    Smart Gen didi
    这玩意。。。感觉一个月以后，没有人能看得懂了
'''
import time,logging, sys
import html_template as ht
import didi_cfg as didi
import random, calendar
import json

cur_billing_end_time = '01/01/1999 00:00'
didi_cfg = dict()
adv_setting = dict()
g_avg = 0
left_times = 0
left_amount = 0

def gen_rand_amount(travel_times, mins):
    global didi_cfg, adv_setting, g_avg, left_times, left_amount
    total_amount = didi_cfg["target_amount"]
    avg_duration = int(sum(adv_setting["duration_range"])/len(adv_setting["duration_range"]))
    amt_inc_per_min = adv_setting["amount_increase_per_minute"]
    # gene avg amount
    real_avg = int(left_amount / left_times)
    real_ctrl_range = abs(g_avg - real_avg) + int(adv_setting["avg_control_range"])
    logging.debug(f'gen_rand_amount() left_times={left_times}, left_amount={left_amount}, mins={mins}, real_avg={real_avg}, real_ctrl_range={real_ctrl_range}')
    if(left_times > 1):
        start = real_avg - real_ctrl_range if real_avg - real_ctrl_range > 0 else 0
        end = real_avg + real_ctrl_range
        logging.debug(f'gen_rand_amount() random range (start, end) = ({start}, {end})')
        real_amount = random.randint(start, end) + ((mins - avg_duration) * amt_inc_per_min) + 100
    elif(left_times == 1):
        real_amount = left_amount + ((mins - avg_duration) * amt_inc_per_min) + 100
    else:
        real_amount = 0
    left_times -= 1
    left_amount -= real_amount
    return int(real_amount/100) * 100


def gen_basic_info(total_amount, billing_month):
    global didi_cfg, adv_setting, g_avg
    avg_amount = adv_setting["avg_amount"]
    avg_ctrl_range = adv_setting["avg_control_range"]
    days_range = adv_setting["days_range"]
    # gene avg amount
    g_avg = random.randint(avg_amount-avg_ctrl_range, avg_amount+avg_ctrl_range)
    trv_times = int(total_amount / g_avg) + 1
    logging.debug(f'gen_basic_info() start total_amount={total_amount}, billing_month={billing_month}, average={g_avg}, travel_times={trv_times}')
    try:
        time.strptime(billing_month, '%Y%m')
    except:
        logging.error('gen_basic_info() billing_month format ERROR, not YYYYMM.')
        return None
    year = int(billing_month[:4])
    month = int(billing_month[4:])
    cal_main = calendar.Calendar()
    monthdays = list()
    weight = list()
    for day in cal_main.itermonthdays2(year, month):
        # (day[0] in days_range if len(days_range)>0 else True) 这一句的意思是如果 days_range 有配置，则判断是否符合日期，如果没有配置，就表示不限制日期
        if(day[0]!=0 and day[1] in [0,1,2,3,4] and (day[0] in days_range if len(days_range)>0 else True)):
            monthdays.append(day[0])
            weight.append(adv_setting["workday_weight"])
        elif(day[0]!=0 and day[1] in [5,6] and (day[0] in days_range if len(days_range)>0 else True)):
            monthdays.append(day[0])
            weight.append(adv_setting["weekend_weight"])
    logging.debug(f'monthdays = {monthdays}')
    logging.debug(f'   weight = {weight}')
    choose_day_list = random.choices(monthdays, weights=weight, k=trv_times)
    choose_day_list.sort()
    logging.debug(f'gen_basic_info() return choose_day_list={choose_day_list}')
    return choose_day_list

def gen_additional_info(choose_day_list, total_amount, billing_month):
    global didi_cfg, adv_setting, g_avg, left_times, left_amount
    avg_amount = adv_setting["avg_amount"]
    avg_ctrl_range = adv_setting["avg_control_range"]
    try:
        time.strptime(billing_month, '%Y%m')
    except:
        logging.error('gen_additional_info() billing_month format ERROR, not YYYYMM')
        return None
    logging.debug(f'gen_additional_info() start total_amount={total_amount}, billing_month={billing_month}')
    # avg = random.randint(avg_amount-avg_ctrl_range, avg_amount+avg_ctrl_range)
    left_amount = total_amount
    travel_times = len(choose_day_list)
    left_times = travel_times

    travel_detail = list()
    home_address = didi_cfg["address_info"]["home"]
    for each_day in choose_day_list:
        billing_day = '%s%02d'%(billing_month, each_day)
        week_day = time.strptime(billing_day, '%Y%m%d').tm_wday
        if(week_day in [5,6]):
            start_time, end_time, mins = gen_billing_time(billing_day, 'weekend')
            # amount = int(((avg + random.randint(-6000, 5000)) + (mins - avg_duration) * amt_inc_per_min) / 100) * 100
            amount = gen_rand_amount(travel_times, mins)
            address_list = didi_cfg["address_info"]["super_market"] + didi_cfg["address_info"]["shopping_mall"] + didi_cfg["address_info"]["other_place"]
            target_address = random.choice(address_list)
            if(random.randint(0,1) > 0):
                add1, add2 = home_address, target_address
            else:
                add1, add2 = target_address, home_address
            travel_detail.append((start_time, end_time, amount, add1, add2))
        else: # must in [0,1,2,3,4]
            start_time, end_time, mins = gen_billing_time(billing_day, 'workday')
            # amount = int(((avg + random.randint(-6000, 5000)) + (mins - avg_duration) * amt_inc_per_min) / 100) * 100
            amount = gen_rand_amount(travel_times, mins)
            address_list = didi_cfg["address_info"]["super_market"] + didi_cfg["address_info"]["shopping_mall"] + didi_cfg["address_info"]["hospital"] + didi_cfg["address_info"]["other_place"]
            weight_list = [5] * len(didi_cfg["address_info"]["super_market"]) + [1] * len(didi_cfg["address_info"]["shopping_mall"]) + \
                [2] * len(didi_cfg["address_info"]["hospital"]) + [1] * len(didi_cfg["address_info"]["other_place"])
            target_address = random.choices(address_list, weights=weight_list, k = 1)[0]
            if(random.randint(0,1) > 0):
                add1, add2 = home_address, target_address
            else:
                add1, add2 = target_address, home_address
            travel_detail.append((start_time, end_time, amount, add1, add2))
    logging.debug(f'travel_detail = {travel_detail}')
    return travel_detail


def gen_billing_time(billing_day, day_type):
    '''
    day_type in ['workday', 'weekend']
    '''
    global cur_billing_end_time, adv_setting
    logging.info(f'gen_billing_time({billing_day}, {day_type}) start.')
    st_billing_day = time.strptime(billing_day, '%Y%m%d')
    st_cur_billing_end_time = time.strptime(cur_billing_end_time, '%d/%m/%Y %H:%M')
    start_sec = int(time.mktime(st_billing_day))
    last_billing_end_time = int(time.mktime(st_cur_billing_end_time))
    travel_range_list = list()
    if(day_type == 'workday'):
        tmp_travel_range_list = adv_setting["workday_travel_hours"].split(',')
    elif(day_type == 'weekend'):
        tmp_travel_range_list = adv_setting["weekend_travel_hours"].split(',')
    else:
        logging.error("gen_billing_time() day_type ERROR!")
        return
    for each_range in tmp_travel_range_list:
        hour_list = each_range.split('-')
        each_start_time = start_sec + (int(hour_list[0]) * 3600)
        each_end_time = start_sec + (int(hour_list[1]) * 3600)
        if(last_billing_end_time <= each_start_time):
        #               |               |-------------|
        #    last_billing_end_time    start          end
            travel_range_list.append({"start":each_start_time, "end":each_end_time})
        elif(each_start_time < last_billing_end_time and last_billing_end_time < each_end_time):
        #               |--------------|-----------------|
        #             start   last_billing_end_time     end
            # last_billing_end_time 需要向后偏移 1800s， 避免两次打车时间太接近
            travel_range_list.append({"start":last_billing_end_time + 1800,"end":each_end_time + 1800})
        elif(last_billing_end_time >= each_end_time):
        #               |----------------|               |
        #             start             end   last_billing_end_time
            # 如果到最后了，一段都没有加进去，为了保证能生成，强行补充一段
            if(len(travel_range_list) == 0 and each_range == tmp_travel_range_list[-1]):
                travel_range_list.append({"start":last_billing_end_time+1800,"end":last_billing_end_time+(1800+3600)})
    logging.debug(f'generate travel_range_list successfule. day_type={day_type}, date={billing_day}')
    for each_range in travel_range_list:
        logging.debug(f'\t Range: ({time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(each_range["start"]))}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(each_range["end"]))})')
    ###############################################################################
    # 先选一段
    pick_travel_range = random.choice(travel_range_list)
    # 然后随机生成开始时间
    start_sec = random.randint(pick_travel_range["start"], pick_travel_range["end"])
    mins = random.randint(adv_setting["duration_range"][0], adv_setting["duration_range"][1])
    end_sec = start_sec + (mins * 60)
    st_start_time = time.localtime(start_sec)
    st_cur_billing_end_time = time.localtime(end_sec)
    string_start_time = time.strftime('%d/%m/%Y %H:%M', st_start_time)
    cur_billing_end_time = time.strftime('%d/%m/%Y %H:%M', st_cur_billing_end_time)
    string_end_time = f'{cur_billing_end_time}'
    logging.info(f'gen_billing_time() end. return=({string_start_time}, {string_end_time}, {mins}).')
    return string_start_time, string_end_time, mins


def assemble_html(travel_detail):
    global didi_cfg
    #Amount, 出发时间, From, 到达时间, To
    total_amount = 0
    detail_list = list()
    for each_line in travel_detail:
        tmp = ht.html_detail%("{:,}".format(each_line[2]), each_line[0], each_line[3], each_line[1], each_line[4])
        detail_list.append(tmp)
        total_amount += each_line[2]
    head = ht.html_part1 % (didi_cfg["name"], "{:,}".format(total_amount), len(detail_list))
    cur_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_name = 'didi_' + cur_time + '.html'
    with open(file_name, 'w', encoding='utf-8') as F:
        F.write(head)
        for each_one in detail_list:
            F.write(each_one)
        F.write(ht.html_part2)
    logging.info(f'assemble_html() generate html file [{file_name}] successful.')

def main():
    global didi_cfg, adv_setting
    with open('didi_cfg.json', 'r', encoding='utf-8')as json_file:
        didi_cfg = json.load(json_file)
    adv_setting = didi_cfg["advance_setting"]
    logger = logging.getLogger()
    if(adv_setting["log_level"] in logging._nameToLevel.keys()):
        logger.setLevel(logging._nameToLevel[adv_setting["log_level"]])
        logger.info(f'Set Current Log Level as [{adv_setting["log_level"]}]')
    logging.info(f'main() Name={didi_cfg["name"]}, Amount={didi_cfg["target_amount"]},Billing_Month={didi_cfg["month"]}')
    logging.info(f'Advance_setting=\n\t{adv_setting}')
    res = gen_basic_info(didi_cfg["target_amount"],didi_cfg["month"])
    logging.info(f'main() from gen_basic_info returns: [{res}]')
    detail = gen_additional_info(res, didi_cfg["target_amount"],didi_cfg["month"])
    assemble_html(detail)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filename=sys.argv[0] + time.strftime("%Y%m%d%H%M%S", time.localtime()) +'.log',
                        filemode = 'w',
                        format='%(asctime)s [line:%(lineno)5d] %(levelname)7s\t %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    main()
    logging.info("-------------Program Finished.-------------")
