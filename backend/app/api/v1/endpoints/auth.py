from fastapi import APIRouter
from app.services import our_hash

auth_router = APIRouter(prefix="",tags =["auth"])

# POST    /auth/login    Loguje użytkownika i tworzy sesję
# GET    /auth/me    Zwraca dane aktualnie zalogowanego użytkownika
# POST    /auth/logout    Kończy sesję

@auth_router.get("")
def get_auth():
    return {"message": "Welcome in authorization service"}



@auth_router.post("/login")
async def post_auth_login():
    
    return

@auth_router.post("/logout")
def post_auth_logout():
    # endpoint login pyta tablicy użytkowników (hash hasła może być bo to nie trudne), 
    # a następnie modyfikuje tablicę sesji (czas wygaśnięcia to np. czas loginu + 3 dni)
    
    return


@auth_router.get("/me")
def get_auth_me():
    # jeżeli użytkownik wykona jakąś aktywność (tj. GET auth/me zostanie poproszony o wyświetlenie jego danych) 
    # i jego sesja jeszcze nie wygasła, to sesja się przedłuża (czas wygaśnięcia to czas sprawdzenia + 3 dni)

    # jeżeli sesja wygasła od ostatniego GET auth/me, zostaje usunięta i prosimy użytkownika o logowanie 

    # jeżeli GET /auth/me zwróci 401 Unauthorized, frontend traktuje użytkownika jako niezalogowanego
    return
