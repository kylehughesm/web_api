from app.data.repository import TrackRepository
from sqlalchemy import text
from app.data.database import init_engine

class PostgresqlTrackRepository(TrackRepository):
    def __init__(self):
        self.engine = init_engine()

    def get_tracks(self, genre_name=None):
        with self.engine.connect() as conn:
            if genre_name is None:
                query = text("""
                select track.name as song, album.title as album, track.composer as artist, genre.name as genre from track
inner join genre on track.genre_id=genre.genre_id 
inner join album on track.album_id=album.album_id;            
                         """)
            else:
                query = text(f"""
                select track.name as song, album.title as album, track.composer as artist, genre.name as genre from track
inner join genre on track.genre_id=genre.genre_id 
inner join album on track.album_id=album.album_id
where genre.name='{genre_name}';
                        """)

            result = conn.execute(query).mappings().all()
            return [dict(row) for row in result]
"""
    def update_status(self, user_id, status):
        # engine.begin() handles the COMMIT automatically for writes
        with self.engine.begin() as conn:
            conn.execute(
                text("UPDATE users SET status = :status WHERE id = :id"),
                {"status": status, "id": user_id}
            )    def update_status(self, user_id, status):
        # engine.begin() handles the COMMIT automatically for writes
        with self.engine.begin() as conn:
            conn.execute(
                text("UPDATE users SET status = :status WHERE id = :id"),
                {"status": status, "id": user_id}
            )
"""
