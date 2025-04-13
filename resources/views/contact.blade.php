<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <script>
        function toggleExtraField(value) {
            document.getElementById('extra').style.display =
                (value === 'other') ? 'block' : 'none';
        }
    </script>
</head>
<body>
    <h1>Contact Form</h1>
    <form method="POST" action="/submit-form">
        @csrf

        <label for="topic">Topic</label>
        <select id="topic" name="topic" onchange="toggleExtraField(this.value)">
            <option value="support">Support</option>
            <option value="sales">Sales</option>
            <option value="advertisement">Advertisement</option>
            <option value="example">Example</option>
        </select>

        <div id="extra" style="display:none;">
            <label for="extra_field">Other Topic</label>
            <input type="text" id="extra_field" name="extra_field">
        </div>

        <label for="message">Message</label>
        <input type="text" id="message" name="message">

        <button type="submit">Send</button>
    </form>
</body>
</html>