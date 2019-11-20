const SET_RESULTS = 'SET_RESULTS';
const SET_QUERY = 'SET_QUERY';
const SET_EXPRESSIONS = 'SET_EXPRESSIONS';
const DELETE_SEARCH = 'DELETE_SEARCH'
const ADD_HAPPY = 'ADD_HAPPY';
const DELETE_ALL = 'DELETE_ALL';


function reducer(state, action) {
    switch (action.type) {
        case DELETE_ALL: {
            return {
                ...state,
                results: [],
                query: '',
                happyCount: 0,
                expressions: []
            }
        }
        case SET_RESULTS: {
            return {
                ...state,
                results: action.data
            }
        }
        case SET_QUERY: {
            return {
                ...state,
                query: action.data
            }
        }
        case SET_EXPRESSIONS: {
            return {
                ...state,
                expressions: action.data
            }
        }
        case DELETE_SEARCH: {
            return {
                ...state,
                results: [],
                query: ''
            }
        }

        case ADD_HAPPY: {
            console.log("in ADD HAPPY", state.happyCount)
            return {
                ...state,
                happyCount: state.happyCount + 1
            }
        }
        default:
            return state
    }
}

export default reducer;
