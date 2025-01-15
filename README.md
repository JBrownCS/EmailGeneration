# Email Generation
You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.

The sales data is saved in a JSON file, and its contents must be manipulated and generated as a pdf. Afterwards, it is sent via email.
The PDF contains a table of all the cars with their ID, Name, Price, and Total Sales. It also mentions the car with the most sales, most revenue, and the most popular car year.
This project was part of the Google IT Automation Program in Course "Automating Real-World Tasks with Python" Module 3. The report.pdf file in the repository is an example of the pdf result before it gets transmitted. The SMTP server may have to be changed for local testing since this was ran on a QwikLabs virtual machine specific to the lab.
