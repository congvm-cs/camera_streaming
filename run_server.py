#!/usr/bin/env python
from server_size.BusNoPaper_app import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=15000, debug=False)