import logging
logging.basicConfig(
    filename = 'app.log',
    filemode = 'a',
    datefmt='%Y-%m-%d %H:%M:%S',
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logging.debug("Это сообщение для отладки (не запишется, так как уровень INFO)")
logging.info("Приложение успешно запущено")
logging.warning("Внимание: низкий заряд батареи или мало места на диске")
logging.error("Не удалось подключиться к базе данных")