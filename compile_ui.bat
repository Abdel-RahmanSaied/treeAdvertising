pyuic5 forms/login_view.ui -o views/login_view.py
pyuic5 forms/main_view.ui -o views/main_view.py

pyuic5 forms/newOrder_view.ui -o views/newOrder_view.py

pyuic5 forms/clients_view.ui -o views/clients_view.py
pyuic5 forms/add_client_view.ui -o views/add_client_view.py

pyuic5 forms/orderRequirment_view.ui -o views/orderRequirment_view.py
pyuic5 forms/add_requirement_view.ui -o views/add_requirement_view.py

pyuic5 forms/followOrder_view.ui -o views/followOrder_view.py
pyuic5 forms/finishedOrders_view.ui -o views/finishedOrders_view.py
pyuic5 forms/orderDetails_view.ui -o views/orderDetails_view.py

pyuic5 forms/inbox_view.ui -o views/inbox_view.py

pyuic5 forms/user_registration_view.ui -o views/user_registration_view.py




pyrcc5  forms/app_resources.qrc -o app_resources_rc.py