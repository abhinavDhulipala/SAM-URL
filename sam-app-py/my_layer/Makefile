# make sure to run in root/sam-app-py directory!!!
build-CustomLayer:
	mkdir -p "$(ARTIFACTS_DIR)/python" && cp $(PWD)/../*.py "$(ARTIFACTS_DIR)/python"
	cp -R ~/.aws/ $(ARTIFACTS_DIR)/python/.aws
	export HOME=$(ARTIFACTS_DIR)/python
