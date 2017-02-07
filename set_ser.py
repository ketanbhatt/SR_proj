import soldier

soldier.run("sudo RABBITMQ_NODE_PORT=5673 RABBITMQ_NODENAME=rb1 rabbitmq-server -detached").output
soldier.run("sudo RABBITMQ_NODE_PORT=5674 RABBITMQ_NODENAME=rb2 rabbitmq-server -detached").output
soldier.run("sudo rabbitmqctl -n rb2 stop_app").output
soldier.run("sudo rabbitmqctl -n rb2 join_cluster rb1@ANIKET").output
soldier.run("sudo rabbitmqctl -n rb2 start_app").output

soldier.run(" sudo rabbitmqctl -n rb1 set_policy ha-all \"\" \'{\"ha-mode\":\"all\",\"ha-sync-mode\":\"automatic\"}\'").output


##soldier.run(rabbitmqctl -n rb1 set_policy ha-all "" '{"ha-mode":"all","ha-sync-mode":"automatic"}')
##Above line must be checked