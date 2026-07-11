from fastapi import APIRouter, status  # pyright: ignore[reportMissingImports]
import uuid
from fastapi import HTTPException # pyright: ignore[reportMissingImports]
from app.schemas import IssueCreate, IssueOut, IssueStatus, IssueUpdate, IssuePriority, Batch_Issue_Create, Design_of_Batch_Issue_Update, Batch_Issue_Update
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", 
                           tags=["Issues"])

@router.get("/", response_model=list[IssueOut])
def get_all_issues():
    "retrives all issues from the database"
    issues = load_data()
    return issues

@router.post("/", response_model=IssueOut, 
                status_code=status.HTTP_201_CREATED)

def create_issue(payload: IssueCreate):
    issues = load_data()
    new_issue={
        "id":str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "status": IssueStatus.OPEN,
        "priority": payload.priority
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.put('/Batch_updation')
async def Batch_put_Operation(payload:Batch_Issue_Update):
    issues=load_data()
    updated,l=0,[]
    for d in payload.issues:
        for issue in issues:
            if issue["id"]==d.id:
                issue["title"] = d.title
                issue["description"] = d.description
                issue["status"] = d.status
                issue["priority"] = d.priority
                updated=1
                break
        if updated==0:
            l.append(d)
        else:
            updated=0
    save_data(issues)
    return "Ids were not found for the followinf ids",l


@router.put('/{issue_id}', response_model=IssueOut)
def update_issue(issue_id: str, payload: IssueUpdate, status_code=status.HTTP_404_NOT_FOUND):
    
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            if payload.title is not None:
                issue["title"] = payload.title
            if payload.description is not None:
                issue["description"] = payload.description
            save_data(issues)
            return issue

    raise HTTPException(status_code=404, detail="Issue not found")



@router.delete('/{issue_id}', response_model=IssueOut)
def IssueDelete(issue_id: str):
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            issues.remove(issue)
            save_data(issues)
            return issue
    #raise HTTPException(status_code=404, detail="Issue not found")


@router.get('/{issue_id}',response_model=IssueOut)
def get_single_issue(issue_id):
    issues=load_data()
    for d in issues:
        if d["id"]==issue_id:
            return d
        
# batch create operation
@router.post('/Batch_Create', response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def Batch__Create_operation(payload: Batch_Issue_Create):
    issues=load_data()
    for d in payload.issues:
        new_issue={
            "id":str(uuid.uuid4()),
            "title": d.title,
            "description": d.description,
            "status": IssueStatus.OPEN,
            "priority": d.priority
        }
        issues.append(new_issue)
        save_data(issues)
    return new_issue


# batch update operation
@router.put('/Batch_updation')
async def Batch_put_Operation(payload:Batch_Issue_Update):
    issues=load_data()
    for d in payload.issues:
        for issue in issues:
            if issue["id"]==d.id:
                issue["title"] = d.title
                issue["description"] = d.description
                issue["status"] = d.status
                issue["priority"] = d.priority
                break            
    save_data(issues)
    return "done"
    


    


