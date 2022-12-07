help: 
	@echo "Commands:"
	@echo " - help: 	show this help"
	@echo " - YEAR= new:		create a new file for today"
	@echo " - readme: 	build the new readme with links"

setup: 
	@touch session.cookie
	@make help

new:
	@python3 src/utils/new_file.py ${YEAR}

readme:
	@python3 src/utils/build_md.py