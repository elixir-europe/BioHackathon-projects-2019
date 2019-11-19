import React from 'react';
import styled from 'styled-components';

const Input = styled.input`
    margin-top: 3rem;
    padding-left: 0.5rem;
    width: 800px;
    font-size:3rem;
    outline: 0;
    border-width: 0 0 4px;
    border-color: black;
    font-family: Dosis;
`

function QuackInput(props) {
    return (
        <div>
            <Input placeholder="type your query" type="search"/>
        </div>
    );
}

export default QuackInput;