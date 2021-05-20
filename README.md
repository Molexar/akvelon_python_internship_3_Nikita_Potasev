# akvelon_python_internship_3_Nikita_Potasev
Tasks for python intern in Akvelon

Here you can see almost completed Task#1:
  ## Models: Transaction: user, amount, date; User: first_name, last_name, email
  
  ### Urls: (/task_1/api)
  1. /users - CRUD methods for User model <br/>
    1. GET - all users <br/>
    2. POST, PUT, DELETE - getting json with all fields <br/>
  2. /transactions - CRUD methods for Transaction model <br/>
  3. /payments - user's Transaction with filters: date, order_by. Getting json with: user_id, date, order_by <br/>
    1. POST - filtering by parameters, getting json with: user, date(2021-01-01 format)
                    date range(date_start, date_end), income/outcome(type of transaction, true), order_by field (-order if we need reversed) <br/>
  4. /payments/<user_id> - History of all user's transactions <br/>
#### In the future will be added some other methods for custom filtering by type of transaction and time period. - Done
