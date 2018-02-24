#!/bin/bash
# wait-for-postgres.sh

hostport=(${1//:/ })
HOST=${hostport[0]}
PORT=${hostport[1]}
shift

wait_for()
{
    while :
    do
        (echo > /dev/tcp/$HOST/$PORT) >/dev/null 2>&1
        result=$?
        if [[ $result -eq 0 ]]; then
            echo "Postgres is up - ready to continue!"
            break
        fi
        echo "Postgres not ready yet. Waiting..."
        sleep 1
    done
    return $result
}

wait_for
RESULT=$?
exit $RESULT
