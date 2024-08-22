#!/bin/bash

PasswordRetrieved=0
while [ $PasswordRetrieved -eq 0 ]; do
    OUT=$(/opt/CARKaim/sdk/clipasswordsdk GetPassword -p 'AppDescs.AppID=ORAASDIKU_U_AIM_178435_User' -p 'Query=Safe=ORAASDIKU_U_AIM_178435_Safe;Folder=Root;Object=ORAAS_MXCGN1U_oraasqrp024_ORAASDIKU_OAAS_UAT_RW' -p 'Reason=test' -p 'FailRequestOnPasswordChange=false' -o 'Password,PasswordChangeInProcess' 2>&1)
    
    if [ $? -ne 0 ]; then
        if [[ $OUT != APPAP282E* ]]; then
            break
        else
            sleep 1.5
        fi
    else
        PasswordRetrieved=1
    fi
done

if [ $PasswordRetrieved -eq 0 ]; then
    echo "$OUT"
else
    echo "$OUT" | awk -F',' '{print $1, $2}'
fi

