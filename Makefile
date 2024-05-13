OUTPUT_FILE = trade

all: $(OUTPUT_FILE)


$(OUTPUT_FILE) : src/trade.py
	cp $< $@
	chmod 777 $@

clean:
	rm -rf $(OUTPUT_FILE)

fclean: clean

re: fclean all