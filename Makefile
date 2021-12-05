PREFIX = /usr

all:
	@echo Run \'make install\' to install dracula-factory.

install:
	@echo $(DESTDIR) is destdir and $(PREFIX) is prefix
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p drf.sh $(DESTDIR)$(PREFIX)/bin/drf
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/drf
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/drfpy
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/drfpy


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/drf
	@rm -rf $(DESTDIR)$(PREFIX)/bin/drfpy
