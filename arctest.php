<?PHP
include_once("ARC/arc/ARC2.php");
include_once("ARC/Graphite.php");

$graph = new Graphite();
$graph -> ns("page", "http://dbpedia.org/page/");
$graph -> ns("resource", "http://dbpedia.org/resource/");
$graph -> ns("prop", "http://dbpedia.org/property/");
$graph -> ns("db-owl", "http://dbpedia.org/ontology/");
$graph -> ns("xsd", "http://www.w3.org/2001/XMLSchema#");
$graph -> ns("category", "http://dbpedia.org/page/Category:");

$graph -> load("http://dbpedia.org/resource/Category:Summer_Olympics_events_by_year");
print $graph -> resource("http://dbpedia.org/resource/Category:Summer_Olympics_events_by_year") -> dump();
?>
<!DOCTYPE html>
<html>
<head>
    <title>DBPedia Queries</title>
</head>
<body>
<div class="container">
<?php echo $result; ?>
<form action="" method="POST" id="dbpedia-queries-form">
    <table id="dbpedia-queries">
        <thead>
            <tr>
                <th>Query nr.</th>
                <th>Vraag</th>
                <th>Query</th>
                <th />
                <th />
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>In welk jaar zijn de eerste olympische winterspelen gehouden?</td>
                <td>
                    <textarea rows="10" cols="20" readonly>
                    SELECT ?date WHERE { :Winter_Olympic_Games dbpedia2:data ?date. }
                    </textarea>
                <td>
                <td>
                    <input type="submit" name="run1" value="Run" />
                </td>
            </tr>
            <tr>
                <td>2</td>
                <td>In welke jaren zijn de olympische zomerspelen gehouden?</td>
                <td>
                    <textarea readonly>
                    </textarea>
                <td>
                <td>
                    <input type="submit" name="run2" value="Run" />
                </td>
            </tr>
            <tr>
                <td>3</td>
                <td>Wie hebben er allemaal bronzen medailles gewonnen voor Tsjecho-Slowakije?</td>
                <td>
                    <textarea readonly>
                    </textarea>
                <td>
                <td>
                    <input type="submit" name="run3" value="Run" />
                </td>
            </tr>
            <tr>
                <td>4</td>
                <td>In welk stadion vond de opening plaats van de winterspelen van 1992?</td>
                <td>
                    <textarea readonly>
                    </textarea>
                <td>
                <td>
                    <input type="submit" name="run4" value="Run" />
                </td>
            </tr>
            <tr>
                <td>5</td>
                <td>Hoeveel landen deden er mee aan de eerste olympische zomerspelen?</td>
                <td>
                    <textarea readonly>
                    </textarea>
                <td>
                <td>
                    <input type="submit" name="run5" value="Run" />
                </td>
            </tr>
        </tbody>
    </table>
</form>
</div>
</body>
</html>

