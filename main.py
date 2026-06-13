    from fastapi import FastAPI
    from posts.router import router as post_router

    app = FastAPI()

    app.include_router(post_router, prefix='/posts', tags=['posts'])


    @app.get('/')
    def index():
        return {"msg":"Main home"}