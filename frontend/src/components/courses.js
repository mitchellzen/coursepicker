import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import React from 'react';
import { Get } from 'react-axios';
import Course from './course';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';
let order = 'desc';
function linkFormatter(cell, row) {
  var url = '/course/' + row.id;
  return '<a href="'+url+'">'+row.id+'</a>';
}
function CourseTable(props){
    return (
        <BootstrapTable ref='table' data={props.courses}>
            <TableHeaderColumn dataField='id' isKey={ true } dataFormat={ linkFormatter } dataSort={ true }>Course ID</TableHeaderColumn>
            <TableHeaderColumn dataField='name' dataSort={ true }>Name</TableHeaderColumn>
            <TableHeaderColumn dataField='cost'>Cost</TableHeaderColumn>
            <TableHeaderColumn dataField='description'>Description</TableHeaderColumn>
        </BootstrapTable>
    )
}
class Courses extends React.Component {
    render() {
        return (
            <div>
                <Get url="http://127.0.0.1:8000/api/courses/?format=json">
                    {(error, response, isLoading) => {
                        if (error) {
                            return (<div>Something bad happened: {error.message}</div>)
                        }
                        else if (isLoading) {
                            return (<div>Loading...</div>)
                        }
                        else if (response !== null) {
                            for(var i=0; i<response.data.length; i++){
                                var path = "/courses/"+response.data[i].id;
                                <Route path={path} component={Course}/>
                            }
                            return (<CourseTable courses={response.data}/>)
                        }
                        return (<div>Default message before request is made.</div>)
                    }}
                </Get>
            </div>
        )
    }
}
export default Courses;