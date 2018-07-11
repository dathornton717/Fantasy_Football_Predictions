const React = require('react');
const ReactDOM = require('react-dom');

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {employees: []};
    }

    componentDidMount() {
        // API invoked after React renders a component in the DOM
    }

    render() {
        return (
               <div>Hello World</div>
        )
    }
}

ReactDOM.render(
<App />,
    document.getElementById('react')
)