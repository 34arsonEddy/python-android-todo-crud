import main
import uuid
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget,IconRightWidget

def deletebtn(main:main,data):
		# LOOP self.alldata  AND CHEK IF id == data id and removeit
		for x in main.alldata:
			if x['id'] == data:
				main.alldata.remove(x)
				print(main.alldata)

				# AND LIST ITEM IN KV FILE THE REMOVE UPDATE DATA
				todo_list = main.screen.ids.todo_list
				for child in todo_list.children:
					if child.id == data:
						todo_list.remove_widget(child)
					# DATA IS UNIQ ID FROM UUID4
# CREATE FUNCTION FOR ADD TODO TO LIST
def addnewtodo(main:main,value):
    print("YOu input is = ",value)
    if value :
        # CREATE UUID FOR EDIT AND DELETE
        item_id = str(uuid.uuid4())
        main.alldata.append(
            {"value":value,"id":item_id}
            )

        # AND GET ID OF KV FILE MDLIST
        todo_list = main.screen.ids.todo_list
        # ADD TO WIDGET IN todo_list SELECTOR
        todo_list.add_widget(
            OneLineAvatarIconListItem(
                IconLeftWidget(
                    icon="pencil",
                    on_release=lambda x:main.editbtn(item_id,value)
                    ),
                IconRightWidget(
                    icon="delete",
                    on_release=lambda x:deletebtn(main,item_id)
                    ),
                id=item_id,
                text=value
                )

            )

    # AND CLEAR INPUT TEXT AFTER CLICK ADD BUTTON
    main.screen.ids.inputtodo.text = ""     