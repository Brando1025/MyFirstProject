.PHONY: all format lint test success

all: format lint test success

format:
	@echo "Running black for code formatting..."
	black .

lint:
	@echo "Running flake8 for linting..."
	flake8 --exclude=.tox

test:
	@echo "Running pytest to execute tests and generate report..."
	pytest --report=report.html --title=测试报告 --tester=Brando --desc=FirstProject  --template=2

success:
	@echo "All tasks completed successfully! Report generated at $(CURDIR)/report.html"
