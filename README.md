# akvelon_python_internship_3_Nikita_Potasev
Tasks for python intern in Akvelon

Here you can see almost completed Task#1:
  ## Models: Transaction: user, amount, date; User: first_name, last_name, email
  
  ### Urls: (/task_1/api)
  1. /users - CRUD methods for User model <br/>
    1. GET - all users <br/>
    2. POST, PUT, DELETE - send json with all fields <br/>
  2. /transactions - get all transaction [GET]
  3. /transaction/<id> - CRUD methods for transaction
  4. /payments - user's Transaction with filters: date, order_by. Getting json with: user_id, date, order_by <br/>
    1. POST - filtering by parameters, send json with: user, date(2021-01-01 format)
                    date range(date_start, date_end), income/outcome(type of transaction, true), order_by field (-order if we need reversed) <br/>
  5. /payments/<user_id> - History of all user's transactions <br/>
  
  ####Instructions of using url: payments[POST]
  1. You can send user_id to get personal information or don't
  2. Next if you send date or date_range you will get filtered transactions
  3. If send income:true or outcome true you will get filtered transactions by type of transaction
  4. And the last one, if send order_by: field or -field you can get ordered transactions by this field

