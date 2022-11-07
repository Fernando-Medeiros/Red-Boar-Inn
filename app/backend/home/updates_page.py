from ..database import Database


class UpdatePage(Database):

    def render_updates(self) -> str:
        html = []
        updates: list[dict] = self.db_updates_find().__reversed__()

        for index, note in enumerate(updates):
            html.append(
                f"""                    
                <div id="version{index}" class="flex flex-wrap w-full h-auto p-2 gap-3 bg-gray-800/5 rounded border border-[#BEBDBF]/10
                                                hover:border-[#BEBDBF]/25">

                    <button type="button" class="p-2 m-auto w-full flex gap-5 justify-between">
                        
                        <span class="bold text-xl flex items-center">
                            { note['version'] }
                            <p class="text-[12px]"> - { note['date'] } </p>     
                        </span>  
                        <ion-icon name="chevron-down-outline" class="text-2xl"></ion-icon>

                    </button>


                    <div id="p_update{index}" class="hidden p-2">
                        <p>
                            { ' <br> '.join(note['info']) }
                        </p>
                    </div>
                    
                </div>
                """
                )
        add_html = "\n".join(html)

        return add_html