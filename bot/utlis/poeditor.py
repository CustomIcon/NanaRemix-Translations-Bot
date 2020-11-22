from aiohttp import ClientSession
import asyncio
from bot import auth, project_id

base_url = 'https://api.poeditor.com/v2/'


async def view_project():
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id
        }
        async with ses.post(
            base_url + 'projects/view',
            data=parameter
        ) as resp:
            return await resp.json()


async def import_translation(files, language):
    async with ClientSession() as ses:
        with open(files, 'rb') as f:
            parameter = {
                'api_token' : auth,
                'id': project_id,
                'updating': 'translations',
                'file': f,
                'language': language,
                'overwrite': '1'
            }
            async with ses.post(
                base_url + 'projects/upload',
                data=parameter
            ) as resp:
                return await resp.json()


async def export_translation(language):
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id,
            'language': language,
            'type': 'yml',
        }
        async with ses.post(
            base_url + 'projects/export',
            data=parameter
        ) as resp:
            return await resp.json()


async def progress_list():
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id,
        }
        async with ses.post(
            base_url + 'languages/list',
            data=parameter
        ) as resp:
            return await resp.json()


async def cont_list():
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id
        }
        async with ses.post(
            base_url + 'contributors/list',
            data=parameter
        ) as resp:
            return await resp.json()


async def add_language(language):
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id,
            'language': language
        }
        async with ses.post(
            base_url + 'languages/add',
            data=parameter
        ) as resp:
            return await resp.json()


async def del_language(language):
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id,
            'language': language
        }
        async with ses.post(
            base_url + 'languages/delete',
            data=parameter
        ) as resp:
            return await resp.json()


async def add_cont(name, email, language):
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id,
            'name': name,
            'email': email,
            'language': language
        }
        async with ses.post(
            base_url + 'contributors/add',
            data=parameter
        ) as resp:
            return await resp.json()


async def del_cont(name, email, language):
    async with ClientSession() as ses:
        parameter = {
            'api_token' : auth,
            'id': project_id,
            'name': name,
            'email': email,
            'language': language
        }
        async with ses.post(
            base_url + 'contributors/remove',
            data=parameter
        ) as resp:
            return await resp.json()
