# appleWatch

This project is so I can parse and push heartrate results from my Apple Watch to my InfluxDB and visualize with Grafana.

You can pull the raw output from your iPhone using the QS Access app into a CSV.
By nature the data isnt well suited for InfluxDB because the watch can take multiple readings
in a single minute and it only records to a minute resolution.
So I added logic to spread data points within the same minute out by 2 seconds.

The parser expects the following
- input file is hr.csv
- you need to remove the leading header line from the CSV file
- you need to remove the trailing blank line from the CSV file
- you need to have a "heartbeat" database in your influx
- your influx is at 127.0.0.1 and does not require credentials
- username tag is gilligan - change to your name
  - this is so you can import multiple users and have them show in different series on the graph

