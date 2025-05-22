from database import Database

def save_to_db(vacancies: List[Dict[str, Any]], region_id: int, db_config: Dict[str, str]) -> bool:
    """Сохраняет вакансии в PostgreSQL."""
    db = Database(**db_config)
    success = db.save_vacancies(vacancies, region_id)
    db.close()
    return success