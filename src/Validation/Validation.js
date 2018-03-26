import React from 'react';

const validation =(props) =>{
  let Message = 'Text Long Enough';
  if (props.InputLength <= 5){
    Message = 'Text too short'
  };
  return (
     <div>
      <p>{Message}</p>
     </div>
   )


}

export default validation;
