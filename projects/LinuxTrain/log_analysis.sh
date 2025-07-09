echo "Top IPs in access.log:"
cat access.log | awk '{print $1}'|sort |uniq -c |sort -nr
cat access.log | awk -F'[:[]' '{print $3":00"}' | sort |uniq -c
cat access.log | awk '{print $7}' |sort | uniq -c |sort -nr
cat access.log | awk '{print $9 == 404}' |wc -l