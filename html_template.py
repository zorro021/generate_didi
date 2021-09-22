html_part1 = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<head>
    <title>Receipt</title>
</head>

<body style="margin: 0; padding: 0;">
    <table cellpadding="0" cellspacing="0" width="100%%" style="padding: 24px 36px">
        <tbody>
            <tr>
                <td>
                    <table align="center" cellpadding="0" cellspacing="0" width="800"
                        style="border-collapse: collapse;">
                        <tbody>
                            <tr>
                                <td>
                                    <table style="padding: 17px 0 30px" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td> <img
                                                    src="https://pt-starimg.didistatic.com/static/starimg/img/1515564055216fbtUSN2gUZIkEVfOzfc.png"
                                                    style="width: 60px; height: 48px;" alt="" /> </td>
                                            <td> <span style="font-size: 28px; color: #999999; margin-left: 27px">Thanks
                                                    to use DiDi</span> </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td> <span style="border-top: 1px solid #E1E2E6; display: block;"></span> </td>
                            </tr>
                            <tr>
                                <td>
                                    <table style="padding: 36px 0 40px" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td style="font-size: 40px; font-weight: bold">Hello %s</td>
                                        </tr>
                                        <tr>
                                            <td style="padding-top: 28px; font-weight: bold"> <span
                                                    style="font-size: 32px;">Total order amount:</span> <span
                                                    style="font-size: 44px; color: #FF7226; margin-left: 20px">
                                                    $%s</span></td>
                                        </tr>
                                        <tr>
                                            <td style="padding-top: 16px;"> <span style="font-size: 28px;">Trip
                                                    Number:</span> <span
                                                    style="padding-left: 16px; font-weight: bold; font-size: 32px; font-weight: bold">%d</span>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td> <span style="border-top: 1px solid #E1E2E6; display: block;"></span> </td>
                            </tr>
                            <tr>
                                <td>
                            <table style="padding-bottom: 40px" cellpadding="0" cellspacing="0">
'''

html_detail = '''
            <tr>
                <td style="font-size: 32px; font-weight: bold; padding-top: 35px">Order
                    Amount: $%s</td>
            </tr>
            <tr>
                <td style="font-size: 26px; font-weight: bold; padding-top: 10px"></td>
            </tr>
            <tr>
                <td style="font-size: 26px"></td>
            </tr>
            <tr>
                <td style="font-size: 26px; color: #999999; padding-top: 20px">
                    <!--出发时间-->%s
                </td>
            </tr>
            <tr>
                <td>
                    <table cellpadding="0" cellspacing="0" style="padding-top: 10px;">
                        <tr>
                            <td> <span
                                    style="width: 12px; height: 12px; background: #00D0AD; border-radius: 100%%; display: inline-block"></span>
                            </td>
                            <td style="font-size: 26px; padding-left: 14px">From: %s
                                </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td style="font-size: 26px; color: #999999; padding-top: 10px">
                    <!--到达时间-->%s
                </td>
            </tr>
            <tr>
                <td>
                    <table cellpadding="0" cellspacing="0" style="padding-top: 10px;">
                        <tr>
                            <td> <span
                                    style="width: 12px; height: 12px; background: #FF7733; border-radius: 100%%; display: inline-block"></span>
                            </td>
                            <td style="font-size: 26px; padding-left: 14px">To: %s</td>
                        </tr>
                    </table>
                </td>
            </tr>
'''

html_part2='''
                                    </table>
                                </td>
                            </tr>
                            <tr style="display: none">
                                <td> <span style="border-top: 1px solid #E1E2E6; display: block;"></span> </td>
                            </tr>
                            <tr style="display: none">
                                <td>
                                    <table style="padding: 40px 0" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td style="font-size: 24px;">place_holder_notice_title</td>
                                        </tr>
                                        <tr>
                                            <td style="font-size: 20px;">place_holder_notice_msg1</td>
                                        </tr>
                                        <tr>
                                            <td style="font-size: 20px;">place_holder_notice_msg2</td>
                                        </tr>
                                        <tr>
                                            <td style="font-size: 20px;">place_holder_notice_msg3</td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td> <span style="border-top: 1px solid #E1E2E6; display: block;"></span> </td>
                            </tr>
                            <tr>
                                <td>
                                    <table style="padding: 40px 0" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td style="font-size: 28px; font-weight: bold">Contact DiDi</td>
                                        </tr>
                                        <tr>
                                            <td style="font-size: 22px; color: #999999; padding-top: 10px">Please
                                                contact us if you have any questions.</td>
                                        </tr>
                                        <tr>
                                            <td style="padding-top: 10px; font-size: 22px; color: #999999;">Email:
                                                pasajero.colombia@didiglobal.com</td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <table style="padding: 50px 0 20px; width: 100%%;" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td
                                                style="text-align: center; padding-top: 10px; font-size: 22px; color: #c2c2c2;">
                                                DiDi Mobility Information Technology Pte. Ltd.152 Beach Road, #14-02,
                                                Gateway East, Singapore 189721</td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body>

</html>
'''