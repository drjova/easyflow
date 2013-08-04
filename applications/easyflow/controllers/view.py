def index():
    """
    """

    response.title = "My workflows"
    response.subtitle = None
    """
    occurrences = \
        db(
            db.occurrence.user_id == auth.user_id).select(
                join = [
                    db.workflow.on(db.occurrence.workflow_id == db.workflow.id),
                    db.status.on(db.occurrence.workflow_id == db.status.workflow_id),
                    db.detail.on(db.detail.status_id == db.status.id),
                ]
        )
    """

    f = open("/tmp/skata", "a")

    results = db(
        ( db.occurrence.user_id == auth.user_id ) & \
        ( db.occurrence.is_active == True )
    ).select(
        db.occurrence.id,
        db.occurrence.name,
        db.occurrence.description,
        db.occurrence.workflow_id,
        db.occurrence.status_id,
        db.workflow.name,
        db.workflow.description,
        db.workflow.logo,
        join = db.workflow.on( db.workflow.id == db.occurrence.workflow_id )
    )

    for result in results:

        workflow_id = result["occurrence"]["workflow_id"]
        occurrence_id = result["occurrence"]["id"]
        status_id = result["occurrence"]["status_id"]

        statuses = db(
            ( db.status.workflow_id == workflow_id )
        ).select(
            db.status.id,
            db.status.name,
            db.status.description,
            db.status.workflow_order,
            orderby = db.status.workflow_order
        )

        for status in statuses:

            status["is_current"] = status["id"] == status_id and True or False

            details = db(
                ( db.detail.status_id == status["id"] )
            ).select(
                db.detail.name,
                db.detail.description,
                db.occurrence_detail.detail_value,
                orderby = db.detail.status_order,
                join = db.occurrence_detail.on( ( db.occurrence_detail.occurrence_id == occurrence_id ) & ( db.occurrence_detail.detail_id == db.detail.id ) )
            )

            status["details"] = details.as_list()

        result["occurrence"]["statuses"] = statuses.as_list()

        f.write(str(result))

    f.write(str("\n\n=================================================\n\n"))
    f.close()

    return dict(results = results, app = "")
