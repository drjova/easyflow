"""
    # -------------------------------------------------------------------- #
    # ------------------        > Workflow object       ------------------ #
    # -------------------------------------------------------------------- #

    Creates a workflow object
    - Workflow
        - Statuses
            - Details
"""
from gluon import current


class Workflow(object):
    def __init__(self):
        # I don't know what
        return None
    def create(workflow,statuses,details):
        """
            # -------------------------------------------------------------------- #
            # ------------------  > Create the workflow object  ------------------ #
            # -------------------------------------------------------------------- #

            @param workflow   : workflow json formated var
            @param statuses   : status json formated var
            @param details    : details json formated var 
            -----------------------------------------------------------------------
            @return: the newly created workflow
                                   
            # ------------------  # Create the workflow object  ------------------ #
        """
        # Fix to see db outside the env.
        db = current.db
        auth = current.auth

        # 1st insert workflow

        # 2nd insert statuses

        # 3rd insert details


        #return self.get(id,2)
        return None
    def get(id=-1,depth=0):
        """
            # -------------------------------------------------------------------- #
            # ------------------  > Return the workflow object  ------------------ #
            # -------------------------------------------------------------------- #

            @param id    : the id of a specific workflow, if -1 (default) return all
            @param depth : the depth 0 : only workflows (default)
                                     1 : workflows and their statuses
                                     2 : workflows, their statuses and their details
            ------------------------------------------------------------------------
            @return: the asked workflows ( Wow :P )            

            # ------------------  # Return the workflow object  ------------------ #
        """
        # Fix to see db outside the env.
        db = current.db
        auth = current.auth 
        # Get all the active occurrences for this user
        occurrences = db(
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
            # TODO: order by date! oldest first
            orderby = ~ db.occurrence.id,
            join = db.workflow.on( db.workflow.id == db.occurrence.workflow_id )
        )

        # For each occurrence get the available statuses and the detail values
        for occurrence in occurrences:

            # Get all the statuses that belong to this occurrence's workflow, in order
            statuses = db(
                ( db.status.workflow_id == occurrence["occurrence"]["workflow_id"] )
            ).select(
                db.status.id,
                db.status.name,
                db.status.description,
                orderby = db.status.workflow_order
            )

            # Add the statuses to our current occurrence
            # TODO: what if we have more occurrences with the same statuses? improve!
            occurrence["status"] = statuses.as_list()
            # Get the total number of statuses for this occurence
            occurrence["occurrence"]["num_statuses"] = len(statuses)

            # Get all the detail values for this occurrence, in order
            details = db(
                ( db.occurrence_status_detail.occurrence_id == occurrence["occurrence"]["id"] )
            ).select(
                db.occurrence_status_detail.status_id,
                db.detail.name,
                db.detail.description,
                db.occurrence_status_detail.detail_value,
                #orderby = db.status.workflow_order | db.detail.status_order,
                orderby = db.detail.status_order,
                distinct = True,
                #join = db.occurrence_detail.on( ( db.detail.id == db.occurrence_status_detail.detail_id ) & ( db.status.id == db.occurrence_status_detail.status_id ) )
                join = db.occurrence_detail.on( db.detail.id == db.occurrence_status_detail.detail_id )
            )

            # Add the detail values to our current occurrence
            occurrence["detail"] = details.as_list()

        return occurrence

    def delete(id):
        # just delete a workflow object   
        return False
        

