pyuic5 forms/login_view.ui -o views/login_view.py
pyuic5 forms/main_view.ui -o views/main_view.py
pyuic5 forms/newOrder_view.ui -o views/newOrder_view.py
pyuic5 forms/chooseDesign_view.ui -o views/chooseDesign_view.py

pyuic5 forms/newOrderData_view.ui -o views/newOrderData_view.py

pyrcc5  forms/app_resources.qrc -o app_resources_rc.py