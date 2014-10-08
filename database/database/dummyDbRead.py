from sql_query import queryRow, queryRowSpecific, queryColumn, queryTable,queryValue,queryValueSpecific

value =queryTable('Devices','name')
print value
valuetwo =queryTable('Setpoints','id')
print valuetwo