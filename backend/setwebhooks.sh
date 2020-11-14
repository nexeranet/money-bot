WEBHOOKS_URL=https://74bcbb9e.eu.ngrok.io
echo '\n############################# deleteWebhook ###################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/deleteWebhook
echo '\n############################ setWebhook ####################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook?url=$WEBHOOKS_URL/webhook
echo '\n############################### getWebhookInfo #################################'
curl https://api.telegram.org/bot$TELEGRAM_TOKEN/getWebhookInfo

