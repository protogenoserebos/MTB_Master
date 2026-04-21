### Install dependences 

- Activate the venv

        source venv/bin/activate

 -Install everything at once

        pip install -r requirements.txt

### Restart Dependencies

- Restart the app server (gunicorn)

        sudo systemctl restart ncmtb.service
    
    > gunicorn was renamed ncmtb.service

- Optional: Restart Nginx to clear any lingering gateway timeouts

        sudo systemctl restart nginx

ncmtb.service                                  loaded active running Gunicorn instance for NCMTB
site1.service                                  loaded active running Gunicorn for DevWriter