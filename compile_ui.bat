pyuic5 forms/login_view.ui -o views/login_view.py
pyuic5 forms/main_view.ui -o views/main_view.py
pyuic5 forms/newOrder_view.ui -o views/newOrder_view.py



pyuic5 forms/notes_view.ui -o views/notes_view.py
pyuic5 forms/followOrder_view.ui -o views/followOrder_view.py
pyuic5 forms/finishedOrders_view.ui -o views/finishedOrders_view.py
pyuic5 forms/orderDetails_view.ui -o views/orderDetails_view.py

pyrcc5  forms/app_resources.qrc -o app_resources_rc.py