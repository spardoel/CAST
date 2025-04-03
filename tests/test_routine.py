import os
from pathlib import Path
os.chdir(Path(__file__).parent.parent) 
print(os.getcwd())
# This will be a linked list object containing Element Objects. 
from element import Element
from routine import Routine

def test_insertAtBegin():
    """
    Test that insertAtBegin works
    """
    r = Routine()
    r.insertAtBegin(Element(id="FX-1-2",name='Double front'))
    r.insertAtBegin(Element(id="FX-4-7",name='Press to handstand'))
    r.printRoutine()
    assert r._head.id == "FX-4-7"
    assert r._head.next.id == "FX-1-2"



def test_insertAtEnd():
    """
    Test that insertAtEnd works
    """
    r = Routine()
    r.insertAtEnd(Element(id="FX-1-2",name='Double front'))
    r.insertAtEnd(Element(id="FX-4-7",name='Press to handstand'))
    r.printRoutine()
    assert r._head.id == "FX-1-2"
    assert r._head.next.id ==  "FX-4-7"

def test_insertAtIndex():
    """
    Test that insertAtIndex works
    """
    r = Routine()
    r.insertAtBegin(Element(id="FX-1-2",name='Double front'))
    r.insertAtBegin(Element(id="FX-4-7",name='Press to handstand'))
    r.insertAtIndex(Element(id="FX-4-45",name='Arabian front'), index=1)
    r.printRoutine()
    r._head.i == "FX-4-7"
    r._head.next.id =="FX-4-45"
    r._head.next.next.i == "FX-1-2"

def test_remove_first_element():
    """
    Test that remove_first_element works
    """
    r = Routine()
    r.insertAtBegin(Element(id="FX-1-2",name='Double front'))
    r.insertAtBegin(Element(id="FX-4-7",name='Press to handstand'))
    r.remove_first_element()
    r.printRoutine()
    r._head.id == "FX-1-2"

def test_remove_element():
    """
    Test that remove_element works
    """
    r = Routine()
    r.insertAtBegin(Element(id="FX-1-2",name='Double front'))
    r.insertAtBegin(Element(id="FX-4-7",name='Press to handstand'))
    r.insertAtBegin(Element(id="FX-4-45",name='Arabian front'))
    r.remove_element(Element(id="FX-4-7",name='Press to handstand'))
    r.printRoutine()
    r._head.id == "FX-4-45"
    r._head.next.id == "FX-1-2"

