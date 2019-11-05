# Team Member
Team Member CRUD

Install Docker, pull repository then

Create .env and .env.db files with below variables

For .env example

	SECRET_KEY=3izb^ryglj(bvrjb2_y1fZvcnbky#358_l6-nn#i8fkug4mmz!
	SQL_ENGINE=django.db.backends.postgresql
	SQL_DATABASE=team_member_db
	SQL_USER=devme
	SQL_PASSWORD=devme_
	SQL_HOST=db
	SQL_PORT=5432
	DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0 
	AWS_ACCESS_KEY_ID=PQR
	AWS_SECRET_ACCESS_KEY=XYZ
	AWS_REGION_NAME=ap-southeast-1

For .env.db example

	POSTGRES_USER=devme
	POSTGRES_PASSWORD=devme_
	POSTGRES_DB=team_member_db
	
	
Then run 

	sudo docker-compose up --build -d
	
Now check this URL in browser 
	http://0.0.0.0/v1/team-member/
