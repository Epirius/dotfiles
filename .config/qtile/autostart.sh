#!/bin/bash
xinput --set-prop "ELAN2204:00 04F3:3109 Touchpad" "libinput Natural Scrolling Enabled" 1     
nitrogen --restore &
/usr/lib/polkit-kde-authentication-agent-1 &    # start authentication agent
