# testproj_for_Arenadata
test task from Arenadata

Test task for QA

Dear candidate for QA Automation Engineer position in Arenadata,
Here is your test task:

Goal
Create a set of automated tests that will cover simple application.

Initial conditions

The app that should be covered with automated tests is located here - https://github.com/dgusakov/test_app
In README.MD you can find some kind of spec. Unfortunately spec is not perfect, but in real life we usually have to deal with specs that can be even worse…
App is meant to be launched in docker so make sure you are able to launch it. (If you are using windows the best option will be to install linux VM or use linux subsystem for windows if you are on WIn10)
What should be in your tests?

There are only 3 mandatory requirements:

    1. All tests should be written using python+pytest
    2. Source code should be published on github.com
    3. We should be able to launch your test so please provide a short readme instruction 


Solution test task:

Run tests  - inside project in terminal write $pytest -v -s. 
First time need command $pip install -r requirements.txt

Setting project - file setting.py(DOMEN_NAME = 'http://0.0.0.0:5000' ),
before testing run docker apptest,

file pytest.ini - setting pytest,

file conftest.py - can switch on logger requests(parameter autouse=True in fixture-function) 

My comment for test task: 

 - no validation format file template(yaml)
 
 - name template is name file loads
 
 - Id should be unique - not work, bug
 
 - have error 500, bug
 
  - I didn't understand the logic "depends" inside yaml-file
  
  - I didn't test the UI, didn't check the clickability of the button in autotests - I didn't have time

