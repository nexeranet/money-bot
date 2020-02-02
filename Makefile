ls :
	ls -lah
bot :
	docker exec -it bot_back bash
db :
	docker exec -it bot_db bash
nginx :
	docker exec -it bot_nginx  /bin/sh
