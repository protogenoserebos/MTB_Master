### Install dependences 

- Activate the venv

        source venv/bin/activate

 -Install everything at once

        pip install -r requirements.txt

### Troubleshoot & Restart Gunicorn Server

sudo systemctl stop ncmtb.service

- To Clear Image Cache

        (venv) root@DevelopWriterUmbrella:/var/www/site2/MTB_Master# rm -rf /var/www/site2/MTB_Master/media/CACHE

        
(venv) root@DevelopWriterUmbrella:/var/www/site2/MTB_Master# sudo systemctl start ncmtb.service

- Restart the app server (gunicorn)

        sudo systemctl restart ncmtb.service
    
    > gunicorn was renamed ncmtb.service

- Optional: Restart Nginx to clear any lingering gateway timeouts

        sudo systemctl restart nginx

ncmtb.service                                  loaded active running Gunicorn instance for NCMTB
site1.service                                  loaded active running Gunicorn for DevWriter