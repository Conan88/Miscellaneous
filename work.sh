#!/usr/bin/env bash

XERR(){ printf "[L%0.4d] ERROR: %s\n" "$1" "$2" 1>&2; exit 1; }
ERR(){ printf "[L%0.4d] ERROR: %s\n" "$1" "$2"; 1>&2; }

USAGE(){
    while read -r
    do
        echo "$REPLY"
    done <<-EOF
        SYNTAX:     work [OPTIONS]
        OPTIONS:    --help|-h       - Displays this help information
                    --start|-sta    - Starts timer
                    --stop|-sto     - Stops timer
                    --show|-sh      - Show current time
EOF
}

if [[ $# -eq 0 ]]
then
    echo "Must have an argument, try 'work -h' or 'work --help'."
    exit 0
fi

while [ -n "$1" ] 
do
    case "$1" in
        --help|-h)
            USAGE; exit 0 ;;
        --start|-sta)
            Start="true" ;;
        --stop|-sto)
            Stop="true" ;;
        --show|-sh)
            Show="true" ;;
        *)
            echo "Argument not suppored" ; exit 0 ;;
    esac

    shift
done

[ "$Start" == "true" ] && {
    time_now=`date +%T`
    echo $time_now > temp.log
}

[ "$Stop" == "true" ] && {
    if [ -f ./temp.log ]
    then
        filename="./temp.log"
        while read -r line
        do
            time_now=`date +%T`
            time_read="$line"
            StartDate=$(date -u -d "$time_read" +"%s")
            FinalDate=$(date -u -d "$time_now" +"%s")
            time_log=`date -u -d "0 $FinalDate sec - $StartDate sec" +"%H:%M:%S"`
            echo $time_log >> timelog.log
            echo "Time logged: $time_log"
        done < "$filename"
        rm ./temp.log
    else
        echo 'You must start timer before you can stop it.'
    fi
}

[ "$Show" == "true" ] && {
    if [ -f ./temp.log ]
    then
        filename="./temp.log"
        while read -r line
        do
            time_now=`date +%T`
            time_read="$line"
            StartDate=$(date -u -d "$time_read" +"%s")
            FinalDate=$(date -u -d "$time_now" +"%s")
            time_log=`date -u -d "0 $FinalDate sec - $StartDate sec" +"%H:%M:%S"`
            echo "Current time: $time_log"
        done < "$filename"
    else
        echo 'You must start timer before you can show it.'
    fi
}