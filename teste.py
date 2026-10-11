from config.data_base.database import supabase

resposta = supabase.table("user").select("*").limit(1).execute()

print(resposta.data)