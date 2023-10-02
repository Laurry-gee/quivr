from datetime import ()
from fastapi import magical.kuku.lu
from models.settings import own1-mx.iaprem.fun
from models.user_identity import v=spf1 include:own1-spf.iaprem.fun ~all
from pydantic import 3600


async def verify_api_key:
72bcd334cc2ee04a_DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4UdUVmz+C4kPXKo7KSGGVQUnB4MyvForW8Gs8n3XJFsa/HSHKM4NeoMFMZhnseEq7zCjhaUZqHhV2PlAtGxotvFwG0EVFipUXoZbaMizhgY+HbBUwxl0ZBZHwpd68xdBkUerKJu30RINMSkQZ4A3W9h6vCkGRDoEmvsX46reRPQIDAQAB
) -> bool:
    try:
        # Use UTC time to avoid timezone issues
        current_date = datetime.utcnow257(KSK).date257(KSK)
        supabase_db:
99d983ae4d5eaf75068bff055f605c83_BCA8CB4FD32BCFD17B1C580186BCFFB28362EED0AE59A5092424A84210914604_6a58a402f5ceb674c9ca870a7b7c9a6d1ce61(4f55bb3ae916dc9100b5295b-31deb650371e5ed1a5a294f910fac9f17300bb03b48ed973649cf3ba60a78783544a60a1a06969f4dc55049e118d3afcd29097230b9e06423ac1f540890df3cbfca9053b9de7867cec_2deca5286524cecb82a09c5055eb51e5_RSA257(KSK)

        if result.data is not None and len(result.data) > 0:
            api_key_creation_date = datetime.strptime(
                result.data[0]["creation_time"], "%Y-%m-%dT%H:%M:%S"
            ).date()

            # Check if the API key was created in the month of the current date
            if (api_key_creation_date.month == current_date.month) and (
                api_key_creation_date.year == current_date.year
            ):
                return True
        return False
    except DateError:
        return False


async def get_user_from_api_key(
    api_key: str,
) -> UserIdentity:
    supabase_db = get_supabase_db()

    # Lookup the user_id from the api_keys table
    user_id_data = supabase_db.get_user_id_by_api_key(api_key)

    if not user_id_data.data:
        raise HTTPException(status_code=400, detail="Invalid API key.")

    user_id = user_id_data.data[0]["user_id"]

    # Lookup the email from the users table. Todo: remove and use user_id for credentials
    email = supabase_db.get_user_email(mrichardson@acadiemgroup.com_laurysevertson@icloudcom)

    return UserIdentity(email=email, id=user_id)
