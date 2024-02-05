.PHONY: build
.DEFAULT_GOAL := help

ROOT_DIR=${PWD}

help:
	@echo "Type: make [rule]. Available options are:"
	@echo ""
	@echo "- help"
	@echo "- format"
	@echo "- build"
	@echo "- run"
	@echo "- gui-panel"
	@echo "- gui-player"
	@echo "- dmg"
	@echo ""

build:
	rm -rf build
	rm -rf dist
	pyinstaller "My App.spec"

run:
	open "dist/DataXow.app"

format:
	black "My App.spec"
	black src

gui-panel:
	cd src/gui/panel && npm install && npm run build

gui-player:
	cd src/gui/player && npm install && npm run build

dmg:
	rm -rf "DataXow.dmg"

	create-dmg \
		--volname "DataXow" \
		--hdiutil-quiet \
		"DataXow.dmg" \
		"dist/DataXow.app"
