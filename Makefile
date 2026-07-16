.PHONY: help test install run clean

help:
	@echo "Доступные команды:"
	@echo " make help - показать справку"
	@echo " make test - запустить тесты"
	@echo " make install - установить зависимости"
	@echo " make run     - запустить CLI"
	@echo " make clean   - удалить временные файлы"
test:
	cd day26 && $(CURDIR)/.venv/bin/python -m pytest
install:
	.venv/bin/python -m pip install -r requirements.txt
run:
	cd day26 && $(CURDIR)/.venv/bin/python -m app.service_cli list
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
