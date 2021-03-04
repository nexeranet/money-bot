WEBHOOKS_URL=https://42327f792034.eu.ngrok.io
echo $WEBHOOKS_URL_NGROK
echo '\n############################# deleteWebhook ###################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/deleteWebhook
echo '\n############################ setWebhook ####################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook?url=$WEBHOOKS_URL/webhook
echo '\n############################### getWebhookInfo #################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/getWebhookInfo

