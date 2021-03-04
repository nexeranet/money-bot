WEBHOOKS_URL=`cat ngrok_host.txt`
echo $WEBHOOKS_URL
echo '\n############################# deleteWebhook ###################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/deleteWebhook
echo '\n############################ setWebhook ####################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook?url=$WEBHOOKS_URL/webhook
echo '\n############################### getWebhookInfo #################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/getWebhookInfo

