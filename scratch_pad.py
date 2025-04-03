from element import Element
from routine import Routine

elm1 = Element(id="FX-1-2",name='Double front')
print(elm1.id)
print(elm1.event)
print(elm1.group)


elm1.printElement()

routine1 = Routine()
routine1.insertAtBegin(elm1)
routine1.printRoutine()

elm2 = Element(id="FX-4-7",name='Press to handstand')
routine1.insertAtIndex(elm2, index=1)
routine1.printRoutine()

elm3 = Element(id="FX-4-45",name='Arabian front')
routine1.insertAtIndex(elm3, index=1)
routine1.printRoutine()



